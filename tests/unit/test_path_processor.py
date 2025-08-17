import pytest
from unittest.mock import Mock, MagicMock
from pptx.util import Emu
from pptweaver.elements.path_processor import PathProcessor

@pytest.fixture
def mock_converter():
    """Fixture to create a mock converter with utility methods."""
    converter = Mock()
    converter.px_to_emu.side_effect = lambda px: Emu(int(px * 12700))
    converter.parse_color.return_value = ((0,0,0), 1.0) # Add default return value
    converter.scale_x = 1.0
    converter.scale_y = 1.0
    return converter

@pytest.fixture
def mock_slide_for_freeform():
    """Fixture to create a mock slide that can handle freeform shapes."""
    slide = Mock()
    freeform_builder = MagicMock()
    slide.shapes.build_freeform.return_value = freeform_builder
    return slide, freeform_builder

def test_path_processor_linearized_points(mock_converter, mock_slide_for_freeform):
    """Tests processing a <path> using its linearized_points attribute."""
    slide_mock, freeform_builder_mock = mock_slide_for_freeform
    element_data = {
        'tagName': 'path',
        'attributes': {
            'd': 'M 10 20 L 50 60 C 80 80 120 80 150 60', # 'd' is ignored
            'linearized_points': '10,20 30,40 50,60 70,70 90,70 110,60'
        },
        'style': {}
    }

    processor = PathProcessor(element_data, slide_mock, mock_converter)
    processor.process()

    # Verify build_freeform was started with the first point
    slide_mock.shapes.build_freeform.assert_called_once_with(
        Emu(10 * 12700), Emu(20 * 12700)
    )
    
    # Verify the rest of the points were passed as the point list
    expected_point_list = [
        (Emu(30 * 12700), Emu(40 * 12700)),
        (Emu(50 * 12700), Emu(60 * 12700)),
        (Emu(70 * 12700), Emu(70 * 12700)),
        (Emu(90 * 12700), Emu(70 * 12700)),
        (Emu(110 * 12700), Emu(60 * 12700)),
    ]
    freeform_builder_mock.add_line_segments.assert_called_once_with(expected_point_list)

    # Verify the shape was finalized
    freeform_builder_mock.convert_to_shape.assert_called_once()
