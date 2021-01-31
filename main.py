try:
    from os import system
    url = input("url:")
    savedPath = input("saved path:")
    if url == "":
        print("Please enter url!")
    else:
        if savedPath == "":
            from os import getcwd
            path = getcwd()
            system(
                f'wget --user-agent="User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36" -c -k -r -p --no-parent --reject "index.html*" {url} -P {path}')
        else:
            system(
                f'wget --user-agent="User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36" -c -k -r -p --no-parent --reject "index.html*" {url} -P {savedPath}')
    system("pause")
except Exception as e:
    print(e)
