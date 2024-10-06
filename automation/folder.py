#for i in range(1,23):
#   f = open (f"chapter{i}.html", "w")


for i in range(1,23):
    with open(f'chapter{i}.html', 'a') as file:
        
        prev_page = i-1 if i>1 else None
        next_page = i+1 if i<22 else None

        #Generating previous link
        if prev_page:
            prev_link = f'''
            <li class="page-item">
                <a class="page-link" href="chapter{prev_page}.html" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                    <span class="sr-only">Previous</span>
                </a>
            </li>
            '''

        else:
                        prev_link = '''
            <li class="page-item disabled">
                <a class="page-link" href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                    <span class="sr-only">Previous</span>
                </a>
            </li>
            '''
        #Doing the same for next_page

          # Generate next link
        if next_page:
            next_link = f'''
            <li class="page-item">
                <a class="page-link" href="chapter{next_page}.html" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    <span class="sr-only">Next</span>
                </a>
            </li>
            '''
        else:
            next_link = '''
            <li class="page-item disabled">
                <a class="page-link" href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    <span class="sr-only">Next</span>
                </a>
            </li>
            '''

                    # Generate page number links
        page_links = ''
        for page_num in range(1, 23):
            if page_num == i:
                page_links += f'''
                <li class="page-item active">
                    <a class="page-link" href="chapter{page_num}.html">{page_num}</a>
                </li>
                '''
            else:
                page_links += f'''
                <li class="page-item">
                    <a class="page-link" href="chapter{page_num}.html">{page_num}</a>
                </li>
                '''

        # Write to file
        file.write(f'''
        <footer>
        <nav aria-label="Page navigation example">
            <ul class="pagination">
                {prev_link}
                {page_links}
                {next_link}
            </ul>
        </nav>
        </footer>
        ''')