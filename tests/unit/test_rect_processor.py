import pytest
from unittest.mock import Mock
from bs4 import BeautifulSoup
from pptx.util import Emu
from pptweaver.elements.rect_processor import RectProcessor

@pytest.fixture
def mock_converter():
    """Fixture to create a mock converter with a px_to_emu method."""
    converter = Mock()
    # Define the behavior of the mock's px_to_emu method
    converter.px_to_emu.side_effect = lambda px: Emu(px * 12700)
    converter.parse_color.side_effect = lambda color_str: ((255, 0, 0), 1.0) # Mock parsing 'rgb(255,0,0)'
    converter.scale_x = 1.0
    converter.scale_y = 1.0
    return converter

def test_rect_processor_attribute_parsing(mock_converter):
    """
    Tests if the RectProcessor correctly parses attributes from the element data.
    """
    # Create a simple SVG rect element as a dictionary, mimicking element_data
    element_data = {
        'rect': {'x': 100, 'y': 50, 'width': 200, 'height': 150},
        'style': {'fill': 'rgb(255, 0, 0)', 'stroke': 'none'},
        'attributes': {}
    }
    
    # Mock slide object, it's needed for initialization but not directly tested here
    mock_slide = Mock()

    # Initialize the processor
    processor = RectProcessor(element_data, mock_slide, mock_converter)

    # The process() method populates the processor's internal attributes
    processor.process()

    # Now, assert that the processor has correctly calculated the pptx attributes
    assert processor.left == Emu(100 * 12700)
    assert processor.top == Emu(50 * 12700)
    assert processor.width == Emu(200 * 12700)
    assert processor.height == Emu(150 * 12700)
    assert processor.fill_color == (255, 0, 0)
