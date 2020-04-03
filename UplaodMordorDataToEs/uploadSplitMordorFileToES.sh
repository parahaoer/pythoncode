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

function getfile(){

    # $1 是 接收的第一个命令行参数
    for file in $1/*
    do
        filename=$(getFileName $file)
        if [[ ${filename} =~ "split_" ]];then
            #当字符串不被任何一种引号包围时，遇到空格就认为字符串结束了，空格后边的内容会作为其他变量或者命令解析
            cmdStr="kafkacat -b ${helk_ip}:9092 -t winlogbeat -P -l $file"
            echo $cmdStr
            `$cmdStr`

            sleep 1s
            echo "wait 1s"
        fi

    done
    

}

helk_ip="172.16.0.16"
getfile /tmp/splitFile