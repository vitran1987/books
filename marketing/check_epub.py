import zipfile

with zipfile.ZipFile('marketing-edtech-guide.epub', 'r') as z:
    print('First 5 files in ZIP:')
    for i, name in enumerate(z.namelist()[:5]):
        info = z.getinfo(name)
        compress_type = 'STORED' if info.compress_type == 0 else 'DEFLATED'
        print(f'{i+1}. {name} - {compress_type}')
    
    print(f'\nTotal files: {len(z.namelist())}')
    
    # Check mimetype
    first_file = z.namelist()[0]
    mimetype_info = z.getinfo('mimetype')
    print(f'\nMimetype check:')
    print(f'  First file: {first_file}')
    print(f'  Compress type: {mimetype_info.compress_type} (0=STORED, 8=DEFLATED)')
    print(f'  Content: {z.read("mimetype").decode()}')
    print(f'  Length: {len(z.read("mimetype"))} bytes')
