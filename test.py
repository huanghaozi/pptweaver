import asyncio
from pptweaver import Converter
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    """
    Main function to run the HTML to PPTX conversion.
    """
    input_html = "tests/samples/about_pptweaver.html"
    
    # Generate a unique output filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_pptx = f"presentation_{timestamp}.pptx"

    if not os.path.exists(input_html):
        logging.error(f"Input file not found: {input_html}")
        return

    logging.info(f"Starting conversion of '{input_html}' to '{output_pptx}'...")
    
    try:
        converter = Converter(input_file=input_html, output_file=output_pptx)
        await converter.convert()
        logging.info(f"Successfully converted and saved to '{output_pptx}'")
    except Exception as e:
        logging.error(f"An error occurred during conversion: {e}")
        # You might want to add more specific error handling here
        # For example, catching Playwright-specific exceptions

if __name__ == "__main__":
    # The asyncio.run() function is a convenient way to run the top-level async main() function.
    # It takes care of getting the event loop, running the task until it's complete,
    # and then closing the loop.
    asyncio.run(main())
