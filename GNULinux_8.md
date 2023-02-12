   1. Создайте скрытую директорию и переместите файл в эту директорию.

	mkdir .hidden_dir
	mv file .hidden_dir/


   2. Одной командой создайте файлы file20-29. Одной командой создайте жёсткие ссылки на эти файлы в скрытой директории. 
Одной командой удалите эти файлы в текущей директории.


	touch file{20..29}
	ln file{20..29} .hidden_dir/
	rm file{20..29}




   3. Создайте символическую ссылку на существующие файл и директорию, а также на несуществующие файл и директорию.

	ln -s existing_file existing_file_symlink
	ln -s existing_dir existing_dir_symlink
	ln -s non_existing_file non_existing_file_symlink
	ln -s non_existing_dir non_existing_dir_symlink



   4. Создайте файл file1 в директории dir1. Переименуйте файл в file2, не заходя в директорию с помощью cd.

	touch dir1/file1
	mv dir1/file1 dir1/file2

