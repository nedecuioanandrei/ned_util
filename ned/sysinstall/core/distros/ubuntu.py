from ned.sysinstall.core.utils.utils import install_from_apt

apt_applications = ["ranger"]

def install() -> None:
    install_from_apt(apt_applications)
