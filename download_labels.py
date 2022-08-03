import zipfile
import os
import wget


cadcd = {
    '2018_03_06': [
        '0001', '0002', '0005', '0006', '0008', '0009', '0010',
        '0012', '0013', '0015', '0016', '0018'
    ],
    '2018_03_07': [
        '0001', '0002', '0004', '0005', '0006', '0007'
    ],
    '2019_02_27': [
        '0002', '0003', '0004', '0005', '0006', '0008', '0009', '0010',
        '0011', '0013', '0015', '0016', '0018', '0019', '0020',
        '0022', '0024', '0025', '0027', '0028', '0030',
        '0031', '0033', '0034', '0035', '0037', '0039', '0040',
        '0041', '0043', '0044', '0045', '0046', '0047', '0049', '0050',
        '0051', '0054', '0055', '0056', '0058', '0059',
        '0060', '0061', '0063', '0065', '0066', '0068', '0070',
        '0072', '0073', '0075', '0076', '0078', '0079',
        '0080', '0082'
    ]
}


for date in cadcd:
    # download file
    calib_url = 'http://wiselab.uwaterloo.ca/cadcd_data/' + date + '/calib.zip'
    calib_filename = wget.download(calib_url)
    # Extract files
    zip = zipfile.ZipFile(calib_filename)
    zip.extractall()
    zip.close()

    os.remove(calib_filename)  # delete zip file
    for folder in cadcd[date]:
        output_path = 'data_labels/' + date + '/' + folder
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        base_url = 'http://wiselab.uwaterloo.ca/cadcd_data/' + date + '/' + folder
        ann_3d_url = base_url + '/3d_ann.json'
        wget.download(ann_3d_url, out=output_path)
        print(f'\nWriting To: {output_path}')
