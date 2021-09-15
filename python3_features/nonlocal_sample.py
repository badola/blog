#!/usr/bin/env python3
import io

def data_generator():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def _write_data(write_callback, batch_size=5):
    # common logic to fetch data

    data_rows_batch = []

    def _writer():
        nonlocal data_rows_batch 
        write_callback(data_rows_batch)
        data_rows_batch = []

    # download huge data lazily(or in batches)
    for data_row in data_generator():
        data_rows_batch.append(data_row)
        if len(data_rows_batch) == batch_size:
            _writer()

    if len(data_rows_batch):
        _writer()

def data_writer(destination):

    if isinstance(destination, io.TextIOBase): # if destination is a file-handle
        if not destination.writable():
            raise AssertionError('file not writable')

        def _file_appender(data_rows):
            # capture destination from outer scope
            nonlocal destination
            for data_row in data_rows:
                destination.write(f'{data_row}\n')
            print(f'[{len(data_rows)}] rows written in file')

        return _write_data(_file_appender)

    else: # assume it is a list

        def _list_appender(data_rows):
            # capture destination from outer scope
            nonlocal destination
            for data_row in data_rows:
                destination.append(f'{data_row}')
            print(f'[{len(data_rows)}] rows written in list')

        return _write_data(_list_appender)


def main():
    download_list = []
    data_writer(download_list)
    print('list-data', download_list)

    download_file = '/tmp/nonlocal_test_file.txt'
    with open(download_file, 'w') as df:
        data_writer(df)
    print(f'file written at {download_file}')

if __name__ == '__main__':
    main()
