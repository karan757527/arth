from os import system
import getpass


def head(title=""):
    system("clear")
    print("-"*140)
    print("Automating LVM By Karan Agrawal".center(140))
    print("-"*140)
    if title:
        print(title.center(140))
        print("-"*140)


def body():
        head()
        print("\n")
        print("-"*140)
        print("+","-"*138,"+",sep="")
        text="""
Choose what you want to do:
1. Display Disks
2. Display Mount Points
3. Display Physical Volumes(PVs)
4. Display Volume Groups(VGs)
5. Display Logical Volumes(LVs)
6. Create Physical Volume(PV)
7. Create Volume Group(VG)
8. Create Logical Volume(LV)
9. Mount the Partition
10. Format the Partition
11. Resize Logical Volume(LV) (Reduce and Extend)
12. Resize Volume Group(VG) (Reduce and Extend)
13. Remove Logical Volume(LV)
14. Remove Volume Group(VG)
15. Remove Physical Volume(PV)
16. Run Custom Linux Command
0. Exit
"""
        for i in text.split("\n"):
                print("| ",i.center(136)," |",sep="")
        print("+","-"*138,"+",sep="")
        choice=input(">>> ")
        return choice


def tasks(ch):
    global kk
    if ch == '1':
        head("Display Disks")
        system("fdisk -l")
    elif ch == '2':
        head("Display Mount Points")
        system("df -hT")
    elif ch == '3':
        head("Display Physical Volumes(PVs)")
        pv = input("Enter name of the PVs or Press Enter to view all PVs\n>>> ")
        system("pvdisplay "+pv)
    elif ch == '4':
        head("Display Volume Groups(VGs)")
        vg = input("Enter name of the VGs or Press Enter to view all VGs\n>>> ")
        system('vgdisplay '+vg)
    elif ch == '5':
        head("Display Logical Volumes(LVs)")
        lv = input("Enter name of the LVs or Press Enter to view all LVs\n>>> ")
        system('lvdisplay '+lv)
    elif ch == '6':
        head("Create Physical Volume(PV)")
        pv=input("Enter location of the PV\n>>> ")
        system("pvcreate " + pv)
    elif ch == '7':
        head("Create Volume Group(VG)")
        vg=input("Enter the name of the VG\n>>> ")
        nopv=(input("Enter the Name of PVs (Seprated by Space)\n>>> "))
        system("vgcreate " + vg +" " + nopv)
    elif ch == '8':
        head("Create Logical Volume(LV)")
        lv = input("Enter the name of LV\n>>> ")
        size=input("Enter the size of LV\n>>> ")
        vg=input("Enter the name of VG\n>>> ")
        system("lvcreate --size {} --name {} {}".format(size,lv,vg))
    elif ch == '9':
        head("Format the Partition")
        lv = input("Enter the name of LV\n>>> ")
        vg=input("Enter the name of VG\n>>> ")
        system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
    elif ch == '10':
        head("Mount the Partition")
        lv = input("Enter the name of LV\n>>> ")
        vg=input("Enter the name of VG\n>>> ")
        path=input("Enter Folder you want LVM to mount upon\n>>> ")
        system("mkdir -p "+path)
        system("mount /dev/{}/{} {}".format(vg,lv,path))
    elif ch == '11':
        head("Resize Logical Volume(LV) (Reduce and Extend)")
        c = input("Reduce/Extend LV (R/E)\n>>> ").upper()
        vg = input('Enter name of VG\n>>> ')
        lv = input('Enter name of LV\n>>> ')
        if c == 'E':
            c='extend'
            s='+'
            size = input('Enter Size by which you want to extend LV\n>>> ')
            system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
            system('resize2fs /dev/{}/{}'.format(vg,lv))
        elif c== 'R':
            size = input('Enter size by which you want to change LV size\n>>> ')
            size2 = input('Enter the final reduced size of LV desired\n>>> ')
            path = input('Enter Mounting Point of LV\n>>> ')
            c='reduce'
            s='-'
            system('umount /dev/{}/{}'.format(vg,lv))
            system('e2fsck -f /dev/{}/{}'.format(vg,lv))
            system('resize2fs /dev/{}/{} {}'.format(vg,lv,size2))
            system('lv{} --size {}{} /dev/{}/{}'.format(c,s,size,vg,lv))
            system('mount /dev/{}/{} {}'.format(vg,lv,path))
        else:
            print("Invalid Choice")            
    elif ch == '12':
        head("Resize Volume Group(VG) (Reduce and Extend)")
        c = input("Reduce/Extend VG (R/E)\n>>> ")
        vg = input("Enter name of the VG\n>>> ")
        pv = input("Enter name of the PV\n>>> ")
        c=c.upper()
        if c == 'E':
            system("vgextend {} {}".format(vg,pv))
        elif c == 'R':
            system('pvmove {}'.format(pv))
            system('vgreduce {} {}'.format(vg,pv))
        else:
            print("Invalid Choice")
    elif ch == '13':
        head("Remove Logical Volume(LV)")
        path = input('Enter LV you want to remove\n>>> ')
        system('umount {}'.format(path))
        system('lvremove {}'.format(path))
    elif ch == '14':
        head("Remove Volume Group(VG)")
        vg = input('Enter VG you want to remove\n>>> ')
        system('vgremove {}'.format(vg))
    elif ch == 15:
        head("Remove Physical Volume(PV)")
        path = input('Enter PV you want to remove\n>>> ')
        system('pvremove {}'.format(path))
    elif ch == '16':
        head("Running Linux Command")
        cmd=input("Enter command you wanna run\n>>> ")
        system(cmd)
    elif ch == '0':
        head("Exitting")
        kk=False	
    else:
        head("Invalid Choice Try Again!!!")


head("Welcome...!Press any key to start configuring LVM")
input()


kk= True
while kk:
        tasks(body())
        input()


head("Thank You")

