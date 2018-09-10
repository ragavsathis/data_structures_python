import re
input_ike_tunnels = list()
input_esp_tunnels = list()



def generate_src_dest_entry_and_yield(ep_list):
    if len(ep_list) % 2:
        raise Exception("src, dest mapping could not be retrieved")
    odd_val_list = [x for x in ep_list if (ep_list.index(x) % 2)]
    even_val_list = [x for x in ep_list if (ep_list.index(x) % 2 == 0)]
    for i in range(len(odd_val_list)):
        yield [even_val_list[i],odd_val_list[i]]

def fetch_and_verify_usr_tunnel_entries(ike_tunnel_entries, esp_tunnel_entries):
    for each_entry in range(len(ike_tunnel_entries)):
        esp_list_per_ike = list()
        print("ike-Entry = {}".format(ike_tunnel_entries[each_entry]))
        print("esp-Entry = {}".format(esp_tunnel_entries[each_entry]))
        ike_entry_generator = generate_src_dest_entry_and_yield(ike_tunnel_entries[each_entry].split(','))
        esp_entry_generator = generate_src_dest_entry_and_yield(esp_tunnel_entries[each_entry].split(','))
        map(lambda x:input_ike_tunnels.append(x), ike_entry_generator)
        map(lambda x: esp_list_per_ike.append(x), esp_entry_generator)
        #input_esp_tunnels.insert(each_entry,list())
        input_esp_tunnels.insert(each_entry,esp_list_per_ike)

def validate_usr_list():
    ike_list_entry = re.split('\s',ike_list)
    esp_list_entry = re.split('\s', esp_list)
    if len(ike_list_entry) != len(esp_list_entry): 
        raise Exception("Mapping between ike & esp could not be retreived")
    fetch_and_verify_usr_tunnel_entries(ike_list_entry, esp_list_entry)
    for each_ike in range(len(input_ike_tunnels)):
        print(input_ike_tunnels[each_ike])
        print(input_esp_tunnels[each_ike])

if __name__ == "__main__":
    #ike_list = "82.20.20.10,82.20.20.100 82.20.20.10,82.20.20.100"
    ike_list = "82.20.20.10,82.20.20.100"
    esp_list = "52.20.20.10,85.20.20.20"
    print("ike_list -{}\nesp_list - {}".format(ike_list, esp_list))
    validate_usr_list()