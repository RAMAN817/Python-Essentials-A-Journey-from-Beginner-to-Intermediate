import os

# Total chapters and existing pages
total_chapters = 24
existing_chapters = [i for i in range(1, 25)]  # Adjust if some chapters are missing

# Read the template file
with open('template.html', 'r') as file:
    template = file.read()

for chapter in existing_chapters:
    # Prepare dynamic content
    chapter_number = chapter
    previous_chapter = chapter - 1 if chapter > 1 else None
    next_chapter = chapter + 1 if chapter < total_chapters else None

    # Previous link
    if previous_chapter:
        previous_link = f'''
        <li class="page-item">
            <a class="page-link" href="chapter{previous_chapter}.html" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">Previous</span>
            </a>
        </li>
        '''
    else:
        previous_link = '''
        <li class="page-item disabled">
            <a class="page-link" href="#" tabindex="-1" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">Previous</span>
            </a>
        </li>
        '''

    # Next link
    if next_chapter:
        next_link = f'''
        <li class="page-item">
            <a class="page-link" href="chapter{next_chapter}.html" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                <span class="sr-only">Next</span>
            </a>
        </li>
        '''
    else:
        next_link = '''
        <li class="page-item disabled">
            <a class="page-link" href="#" tabindex="-1" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                <span class="sr-only">Next</span>
            </a>
        </li>
        '''

    # Page numbers
    page_numbers = ''
    for i in existing_chapters:
        if i == chapter:
            page_numbers += f'<li class="page-item active"><a class="page-link" href="chapter{i}.html">{i}</a></li>\n'
        else:
            page_numbers += f'<li class="page-item"><a class="page-link" href="chapter{i}.html">{i}</a></li>\n'

    # Replace placeholders in the template
    page_content = template.replace('{{chapter_number}}', str(chapter_number))
    page_content = page_content.replace('{{previous_link}}', previous_link)
    page_content = page_content.replace('{{next_link}}', next_link)
    page_content = page_content.replace('{{page_numbers}}', page_numbers)

    # Write to the chapter HTML file
    output_filename = f'chapter{chapter}.html'
    with open(output_filename, 'w') as output_file:
        output_file.write(page_content)

    print(f'Generated {output_filename}')
