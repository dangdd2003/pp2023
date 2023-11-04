import subprocess
# subprocess only use for implementation of first argument
# no use for whole commandline

def parse(cmd_str):
    token = cmd_str.split()
    argv = []

    # command = [prog, argv] + in_symbol + "file" + out_symbol + "file"
    in_sym = None
    out_sym = None
    cmd = {"program": [], "in": None, "out": None}
    for tok in token:
        if tok == "|":
            argv.append(cmd)
            cmd = {"program": [], "in": None, "out": None}
        else:
            if tok == "<":
                in_sym = 1
                continue
            elif tok == ">":
                out_sym = 1
                continue

            if in_sym:
                cmd["in"] = tok
            elif out_sym:
                cmd["out"] = tok
            else:
                cmd["program"].append(tok)
            in_sym = out_sym = 0
    argv.append(cmd)
    return argv

def execvp(cmd, pipe_out=None):

    f_out = None
    f_in = None
    cap = True

    if cmd["out"]:
        f_out = open(cmd["out"], "wb")
        cap = False
    if cmd["in"]:
        f_in = open(cmd["in"], "rb")
    elif pipe_out:
        f_in = pipe_out
    prog = cmd["program"]
    result = subprocess.run(prog, capture_output=cap, stdin=f_in, stdout=f_out)
    if f_in and not pipe_out:
        f_in.close()
    if f_out:
        f_out.close()
    return result

if __name__ == "__main__":
    pipe_out = None
    result = None

    while True:
        cmd = input("shell>")
        argv = parse(cmd)
        if cmd == "exit":
            exit()
        print(f"shell>{argv}")
