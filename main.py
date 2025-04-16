import frontend

def main():
    manager = frontend.interfaces()
    try:
        manager.main()
    
    except KeyboardInterrupt:
        print("\n usuário saiu")

if __name__ == "__main__":
    main()
