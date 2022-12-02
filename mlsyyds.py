import torch
device = torch.device('cuda:0')  # with referenve to the specific free cuda ID
a=torch.zeros(2,1)
b = a.to(device)
print(b)

#print(torch.cuda.is_available())