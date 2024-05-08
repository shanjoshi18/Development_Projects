from read_files import FileProcessing



if __name__ == '__main__':
    input_path = "D:/fileprocessing/input"
    out_path = "D:/fileprocessing/output/RESULT.csv"
    fileprocessor = FileProcessing(input_path, out_path)
    files = fileprocessor.list_files()
    data_frames = fileprocessor.read_files(files)
    filtered_data = fileprocessor.filter_dataframes(data_frames)
    print(filtered_data)
    fileprocessor.save_file(filtered_data)

