import os
import shutil

class Relocate:

    def copyr(self, origin, destination):
        # Copy something into a new location
        entry = origin
        exit = destination
        shutil.copy(entry, exit)

    def movr(self, origin, destination):
        # o = origin
        entry = origin
        exit = destination
        shutil.move(entry, exit)

# For running as a script
go = Relocate()

print("First, let's make a copy.")
print("What is the source file?")
copy_origin = input("filename >> ")
copy_dest = input("copy name >> ")
go.copyr(copy_origin, copy_dest)
print("")
print("Done!")
print("")

print("Now let's move the file into a new location.")
move_origin = input("filename >> ")
move_dest = input("Destination name >> ")
go.movr(move_origin, move_dest)
print("")
print("Done!")
print("")

print("Now check your file explorer to find your new file in its new location.")
