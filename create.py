import xml.etree.cElementTree as et
import uuid

def make_config(name, disk_path, ram, vcpu):
    domain = et.Element("domain")

    namexml = et.SubElement(domain, "name")
    namexml.text = name

    uuidxml = et.SubElement(domain, "uuid")
    uuidxml.text = str(uuid.uuid1())

    memoryxml = et.SubElement(domain, "memory")
    memoryxml.set("unit", "MB")
    memoryxml.text = ram

    cmemoryxml = et.SubElement(domain, "currentMemory")
    cmemoryxml.set("unit", "MB")
    cmemoryxml.text = ram

    vcpuxml = et.SubElement(domain, "vcpu")
    vcpuxml.set("placement", "static")
    vcpuxml.text = vcpu

    osxml = et.SubElement(domain, "os")
    
    typexml = et.SubElement(osxml, "type")
    typexml.text = "hvm"

    bootdev1xml = et.SubElement(osxml, "boot")
    bootdev1xml.set("dev", "hd")

    featurexml = et.SubElement(domain, "features")
    acpixml = et.SubElement(featurexml, "acpi")
    apicxml = et.SubElement(featurexml, "apic")
    paexml = et.SubElement(featurexml, "pae")

    clockxml = et.SubElement(domain, "clock")
    clockxml.set("offset", "utc")

    onpoweroffxml = et.SubElement(domain, "on_poweroff")
    onpoweroffxml.text = "destroy"

    onrebootxml = et.SubElement(domain, "on_reboot")
    onrebootxml.text = "restart"

    oncrashxml = et.SubElement(domain, "on_crash")
    oncrashxml.text = "restart"
    
    devicesxml = et.SubElement(domain, "devices")

    emulatorxml = et.SubElement(devicesxml, "emulator")
    emulator.text = "/usr/libexec/qemu-kvm"

    disk1xml = et.SubElement(devicesxml, "disk")
    disk1xml.set("type", "file")
    disk1xml.set("device", "disk")

    disk1driverxml = et.SubElement(disk1xml, "driver")
    disk1driverxml.set("name", "qemu")
    disk1driverxml.set("type", "raw")
    disk1driverxml.set("cache", "none")

    disk1sourcexml = et.SubElement(disk1xml, "source")
    disk1sourcexml.set("file", "/var/disks/vm%s" % str(name))
    
    disk1targetxml = et.SubElement(disk1xml, "target")
    disk1targetxml.set("dev","hda")
    disk1targetxml.set("bus","ide")

    disk1addressxml = et.SubElement(disk1xml, "address")
    disk1addressxml.set("type", "drive")
    disk1addressxml.set("controller", "0")
    disk1addressxml.set("bus", "0")
    disk1addressxml.set("target", "0")
    disk1addressxml.set("unit", "0")

    disk2xml = et.SubElement(devicesxml, "disk")
    disk2xml.set("type", "block")
    disk2xml.set("device", "cdrom")

    disk2driverxml = et.SubElement(disk2xml, "driver")
    disk2driverxml.set("name", "qemu")
    disk2driverxml.set("type", "raw")

    disk2targetxml = et.SubElement(disk2xml, "target")
    disk2targetxml.set("dev","hdc")
    disk2targetxml.set("bus","ide")

    disk2readonlyxml = et.SubElement(disk2xml, "readyonly")

    disk2addressxml = et.SubElement(disk2xml, "address")
    disk2addressxml.set("type", "drive")
    disk2addressxml.set("controller", "0")
    disk2addressxml.set("bus", "1")
    disk2addressxml.set("target", "0")
    disk2addressxml.set("unit", "0")

    tree = et.ElementTree(domain)
    path = "/var/configs/vm%s.xml" % str(name)
    tree.write(path)
