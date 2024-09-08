from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('pyqt_phone_input', excludes=['hooks'])