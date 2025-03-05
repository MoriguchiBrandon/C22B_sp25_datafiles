def get_gene(file_contents):
    Dm_Ds = []
    for row in file_contents.split("\n"):
        if "Drosophila melanogaster" in row or "Drosophila simulans" in row:
            Dm_Ds.append(row)
    return Dm_Ds

def gene_exp(data):
    output = []
    for row in data:
        split = row.split(",")
        at_percent = (split[1].count("a") + split[1].count("t")) / len(split[1])
        if at_percent > 0.65:
            output.append(f"{split[2]} has high AT content")
        elif at_percent < 0.45:
            output.append(f"{split[2]} has low AT content")
        else:
            output.append(f"{split[2]} has medium AT content")
    print("Gene AT Content Analysis Results:")
    for line in output:
        print(line)    
    return output
 

if __name__ == "__main__":
    file_obj = open("drosphila.csv")
    file_contents = file_obj.read()

    data = get_gene(file_contents)
    
    output = gene_exp(data)
    
    assert "kdy647 has high AT content" in output[0]
    assert "jdg766 has medium AT content" in output[1]
    
