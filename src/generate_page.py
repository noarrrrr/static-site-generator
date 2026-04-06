import os
from htmlnode import markdown_to_html_node
from markdown_blocks import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    content = None
    for file in os.listdir(from_path):
        if file.endswith(".md"):
            f = open(f"{from_path}/{file}")
            content = f.read()
        elif os.path.isdir(f"{from_path}/{file}"):
            generate_page(f"{from_path}/{file}", template_path, f"{dest_path}/{file}", basepath)
    if not content:
        return
    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    f = open(template_path)
    template = f.read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    if not os.path.isdir(dest_path):
        os.makedirs(dest_path)
    with open(f"{dest_path}/index.html", "w") as f:
        f.write(template)