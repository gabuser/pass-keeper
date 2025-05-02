import frontend

def main():
    #manager varible to call the frontend file to execute the program, it's an object that stands for password manager or a global object
    manager = frontend.interfaces()
    try:
        manager.main()
    
    except KeyboardInterrupt:
        print("\n usuário saiu")

if __name__ == "__main__":
    main()
