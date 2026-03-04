from encryption import encryptMsg, decryptMsg
from hideNseek import storeMsg , retrieveMsg
import time



def main_menu():
    while True:
        print("\n\n\n--- GHOSTPIXEL COMMAND CENTER ---\n")
        print("1. [ENCRYPT] Hide a message inside an image")
        print("2. [DECRYPT] Retrieve a message from an image")
        print("3. [EXIT] Close System")
        print("-" * 33)
        
        choice = input("Select an option (1-3): ").strip()
        print()
        print()

        if choice == '1':
            print("\n[!] Starting Encryption Sequence...\n")

            msg = input("Enter the Password/Message to store: ")
            encmsg = encryptMsg(msg)

            print("\nMessage encrypted successfully")
            print("Select the image to store the message in.")

            storing = storeMsg(encmsg.getEncMsg())
            print("Encrypted message stored successfully in the image.")

            print("\nSelect a folder to save the image")
            storing.saveImg()

            input("\nPress Enter to return to menu...")
            
        elif choice == '2':
            print("\n[!] Starting Decryption Sequence...\n\n")
            print("Select the image.")
            
            storedIn = retrieveMsg()
            retrievedmsg = storedIn.getEncMsg()
            print("Message retrieved successfully from the image.\n")

            decrmsg = decryptMsg(retrievedmsg)
            print("\nMessage decrypted successfully.")

            msg = decrmsg.getDecrMsg()
            print("\n\nSecured Note Retrieved:",msg)


            input("\nPress Enter to return to menu...")
            
        elif choice == '3':
            print("\nShutting down GhostPixel. Stay safe.")
            break
            
        else:
            print("\n[ERROR] Invalid selection. Please try again.")







splash = r"""
    ############################################################
    #                                                          #
    #     _____ _                      _   _____ _             #
    #    |  __ \ |                    | | |  __ (_)            #
    #    | |  \/ |__   ___  ___ ______| |_| |__) |__  _____| | #
    #    | | __| '_ \ / _ \/ __|______| __|  ___/ \ \/ / _ \ | #
    #    | |_\ \ | | | (_) \__ \      | |_| |   | |>  <  __/ | #
    #     \____/_| |_|\___/|___/       \__|_|   |_/_/\_\___|_| #
    #                                                          #
    #                SECURE STEGANOGRAPHY SYSTEM               #
    #          [ AES-256 GCM + PBKDF2 KEY DERIVATION ]         #
    ############################################################
    """
print(splash)
time.sleep(0.7)
print("    Initializing GhostPixel engine...")
time.sleep(0.7)
print("    Checking cryptographic modules... [OK]")
time.sleep(0.7)
print("    System ready. No traces left.\n")
time.sleep(0.7)

main_menu()

