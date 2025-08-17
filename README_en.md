# 幻织 (PPTWeaver) ✨ - My Personal Quest to Bridge AI and Editable Slides

Hi there! This is a personal project born from a simple question: "Can I get AI to create *truly editable* PowerPoint slides?" This is the story of that experiment.

[中文](./README.md) | **English**

---

### 🤔 The Problem: AI PPT Tools Felt... Off

Like many, I was amazed by AI's ability to generate content. But when I looked into AI PPT generators, I found they generally fall into a few categories, none of which felt quite right:

1.  **Template Fillers**: These tools take your text and pour it into predefined templates. They're fast, but creatively restrictive. You can't ask for a complex, custom diagram because the AI is just filling in boxes.
2.  **Image Exporters**: These offer more visual freedom, but they cheat. They generate beautiful slides as static images or PDFs. This completely misses the point of PowerPoint—you can't edit anything!
3.  **Walled Gardens**: Powerful tools like Microsoft Copilot are deeply integrated but are often paid, closed-source products. For a developer who likes to tinker, they're a black box.

### ✨ The "Aha!" Moment: AI is a Master of HTML & SVG

The breakthrough came when I realized I was asking the wrong question. Instead of "AI, make me a PPT," I should have been asking, "AI, make me the *visuals* for a PPT."

It turns out, Large Language Models are **phenomenal** at generating complex, beautiful, and precise visuals using HTML and SVG. This is a language they understand natively. Suddenly, I had a way to create any custom chart, diagram, or layout I could imagine.

But this led to a new challenge: how do you get this perfect web-based content into a fully editable `.pptx` file?

### 🛠️ The Solution: PPTWeaver's Workflow

This project is my answer. Instead of treating the AI like a slide designer, I treat it like a web developer. The workflow looks like this:

[View the PPTWeaver Workflow Diagram](docs/about_pptweaver_workflow.svg)

1.  **HTML/SVG as the Source**: We start with a standard HTML file. Each `<body>` tag represents a new slide.
2.  **Render with a Headless Browser**: PPTWeaver uses Playwright to render the HTML in the background, exactly as a browser would. This captures all CSS styling and layout information with perfect fidelity.
3.  **Extract & Translate**: The core engine then inspects the rendered page, extracts every SVG element, and translates its properties (position, size, color, text) into the language of `python-pptx`.
4.  **Weave the PPTX**: Finally, it reconstructs each element as a native, editable PowerPoint shape, weaving the web content into a final `.pptx` file.

### 🏛️ Software Architecture

Here's a more detailed look at how the components fit together:

[View the PPTWeaver Software Architecture Diagram](docs/architecture.svg)

### 🚀 Give It a Go!

**Installation:**
```bash
# Install the package
pip install pptweaver
# Install Playwright dependencies (needed on first use)
playwright install
```

**Quick Usage:**
```python
import asyncio
from pptweaver import Converter

async def main():
    converter = Converter(input_file="your_slides.html", output_file="presentation.pptx")
    await converter.convert()

asyncio.run(main())
```

### 🚧 Work in Progress & Future Plans

This is still very much a work in progress! Here's a rough idea of what's on the roadmap:

-   [ ] **Improved Style Conversion**: Better support for CSS gradients, shadows, and complex text styling.
-   [ ] **Animation & Transitions**: Basic support for slide transitions and simple entrance animations.
-   [ ] **Interactive Elements**: Exploring ways to map HTML links or buttons to interactive PowerPoint elements.
-   [ ] **Direct Prompt-to-PPTX**: A higher-level API that integrates with an LLM to go from a text prompt directly to a finished PPTX file.
-   [ ] **More Processors**: Support for more niche SVG tags and CSS properties.

### 🤝 Let's Build Together!

This is a personal project, and I'd love for it to be a community one. If you have ideas, find a bug, or want to add a feature, please open an Issue or submit a Pull Request!
