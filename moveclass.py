import os
import shutil

class Relocate:

    def copyr(self, origin, destination):
        # Copy something into a new location
        o = origin
        d = destination
        shutil.copy(o, d)

    def movr(self, origin, destination):
        o = origin
        d = destination
        # Move something into a new location
        shutil.move(o, d)

# For running as a script
go = Relocate()

print("First, let's make a copy.")
print("What is the source file?")
copyorigin = input("filename >> ")
copydest = input("copy name >> ")
go.copyr(copyorigin, copydest)
print("")
print("Done!")
print("")

print("Now let's move the file into a new location.")
moveorigin = input("filename >> ")
movedest = input("Destination name >> ")
go.movr(moveorigin, movedest)
print("")
print("Done!")
print("")

print("Now check your file explorer to find your new file in its new location.")
