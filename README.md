# Edgedb RCE exploitation code

This is a small script to exploit the RCE vulnerability in pickle of edgedb.

---

## Vulnerability: Insecure Deserialization 

The vulnerability is in the pickle.loads() function, which executes a command when you provide an os.system command as object.

The pickle.loads() which this code uses is found under /edb/server/compiler_pool/server.py on line 433

Github (vulnerable version):  [https://github.com/edgedb/edgedb/tree/25edd1dd5d4ac2dab80f06e1b6f8f47e167a3b90](https://github.com/edgedb/edgedb/tree/25edd1dd5d4ac2dab80f06e1b6f8f47e167a3b90)

More about insecure deserialization: https://portswigger.net/web-security/deserialization

---

## Code

Since this application doesnt communicate in HTTP if not configured, we need to make this request with an TCP-pakage.

The script connects itself to the given IP and Port with a socket. Generates the object with the command (in this case “xdg-open /”) calculates the length of the payload (the reason why is found in the edgedb source-code).

After that it packs everything together with the same uint64 packer as in edgedb, adds some extra bytes (for the id of the request, reason again found in the edgedb source-code) and sends that packet.
