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
    file_path=$1

    if [ "${file_path##*.}"x = "json"x ];then
        file_name=$(getFileName $file_path)

        # split -l 指定分割后文件的行数， "split_${file_name}"是分割后文件名的前缀。
        split -l 1000 $file_path "split_${file_name}"
    fi
}

#遍历当前目录 及其子目录中的文件， 如果子目录为空，可能会陷入死循环
function getdir(){

    # $1 是 接收的第一个命令行参数
    for file in $1/*
    do
        if test -f $file
        then
                splitBigFile $file
                #arr=(${arr[*]} $file)
        else
                getdir $file
        fi
    done
}

getdir .






