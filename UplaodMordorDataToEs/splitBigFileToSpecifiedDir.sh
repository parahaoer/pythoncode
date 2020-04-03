function getFileName() {
    filepath=$1
    #获取目录名
    dir=${filepath%/*}
    #获取带后缀的文件名
    filefullname=${filepath##*/}
    #获取不带后缀的文件名
    filename=${filefullname%%.*}
    echo $filename
}


function splitBigFile() {

    cd /tmp/splitFile
    file_array=$1
    for file_path in ${file_array[*]};
    do
        if [ "${file_path##*.}"x = "json"x ];then
            file_name=$(getFileName $file_path)
            # split -l 指定分割后文件的行数， "split_${file_name}"是分割后文件名的前缀。
            split -l 1000 $file_path "split_${file_name}"
        fi
    done
}

#遍历当前目录 及其子目录中的文件， 如果子目录为空，可能会陷入死循环
function getdir(){

    i=$2
    file_array=$3
    for file in $1/*
    do
        if test -f $file
        then
            file_array[i]=$file
            i=$[$i+1]
        else
            getdir $file $i $file_array
        fi
    done
}


if [ ! -d "/tmp/splitFile" ];then
    mkdir /tmp/splitFile
fi

i=0
file_array=()

# 获取当前文件的绝对路径
work_path=$(dirname $(readlink -f $0))

# 将当前目录及其子目录的文件绝对路径 添加到数组file_array中
getdir $work_path $i $file_array

# 在指定目录/tmp/splitFile中, 将文件列表中的文件分割成小文件
splitBigFile $file_array






