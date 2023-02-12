1. Создайте 5 файлов 5 командами(1), одной командой (2) и одной командой с помощью регулярных выражений (3).

(1)
touch file1
touch file2
touch file3
touch file4
touch file5

(2)
touch file1 file2 file3 file4 file5

(3)
touch file{1..5}


2. Создайте скрытую директорию и скрытый файл внутри этой директории.

mkdir .hidden_dir
touch .hidden_dir/.hidden_file


3. Одной командой создайте 3 скрытые директории(dira,dirb,dirc), так, чтобы 2 директории(dirb,dirc) были вложены в первую(dira).

mkdir -p .dira/.dirb .dira/dirc


4. Создайте скрытые копии файлов в скрытой директории

cp file1 .hidden_dir/.file1_copy
cp file2 .hidden_dir/.file2_copy
cp file3 .hidden_dir/.file3_copy
cp file4 .hidden_dir/.file4_copy
cp file5 .hidden_dir/.file5_copy

5. Скопируйте скрытые копии файлов из скрытой директории в текущую директорию так, чтобы они перестали быть скрытыми.

cp .hidden_dir/.file1_copy file1_copy
cp .hidden_dir/.file2_copy file2_copy
cp .hidden_dir/.file3_copy file3_copy
cp .hidden_dir/.file4_copy file4_copy
cp .hidden_dir/.file5_copy file5_copy

6. Создайте жёсткую ссылку на файл с помощью команды cp.

ln file1 file1_link


7. Скопируйте скрытую директорию dira в новую директорию dird.

cp -R .dira dird

