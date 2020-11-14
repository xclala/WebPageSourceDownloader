try:
    from os import system
    url = input("url:")
    savedPath = input("saved path:")
    if url == "":
        print("请输入url!")
    else:
        if savedPath == "":
            from os import getcwd
            path = getcwd()
            system(
                f'wget -c -k -r --no-parent --reject "index.html*" {url} -P {path}')
        else:
            system(
                f'wget -c -k -r --no-parent --reject "index.html*" {url} -P {savedPath}')
    system("pause")
except Exception as e:
    print(e)
