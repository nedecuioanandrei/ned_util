def install(args):
    match args.distro:
        case "ubuntu":
            print("Instalam ce trebuie pe ubuntu.\nIl facem sa toarca pe motan.")
            from ned.sysinstall.core.distros.ubuntu import install 
            install()
        case _:
            print("Sa moara 23% din matusa mea Mircea de stiu sa instalez ce vrei.")
