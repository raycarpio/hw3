pages = [
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "My Blog",
    },
    {
        "filename": "content/contactme.html",
        "output": "docs/contactme.html",
        "title": "Contact Me",
    },
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Welcome to my Website!",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects",
    },
]



def main():
    for page in pages:
        template = open("templates/base.html").read()
        content = open(page["filename"]).read()
        combined_page = template.replace("{{content}}", content)
        combined_page_with_title = combined_page.replace("{{title}}", page["title"])
        open(page["output"], "w+").write(combined_page_with_title)
    
main()
