import socket 
import time 
def scan_host(host, port_start=1, port_end=8000, timeout=0.5):
    open_port=[]
    start = time.perf_counter()
    for port in range(port_start, port_end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            result = s.connect_ex((host,port))
            if result == 0:
                open_port.append(port)
        except socket.timeout:
            pass
        except socket.error as e:
            print("Socket error on port:",{e})
        finally:
            try:
                s.close()
            except Exception:
                pass
    elapsed_time = time.perf_counter() - start
    return open_port, elapsed_time

if __name__ == "__main__":
    host = input("enter the INET(127.0.0.1 is prefered for local testing)").strip().lower()
    open_port, elapsed_time = scan_host(host, 1, 8000, timeout=0.5)
    print(f"Open port: {open_port}\nScan time: {elapsed_time:.2f}s")
