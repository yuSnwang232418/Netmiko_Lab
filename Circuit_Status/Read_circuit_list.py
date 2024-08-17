from collections import defaultdict


def read_circuit_list():
    ping_list = defaultdict(list)
    with open("Circuit_list.txt", "r") as f:
        contents = f.read().splitlines()
        # print(contents)
        for content in contents:
            cur_con = content.split(',')
            # print(cur_con)
            ping_list[cur_con[0]].append((cur_con[1],f"ping {cur_con[4]} so {cur_con[2]}"))
            ping_list[cur_con[0]].append((cur_con[3],f"ping {cur_con[2]} so {cur_con[4]}"))
        # print(ping_list)
        return ping_list
