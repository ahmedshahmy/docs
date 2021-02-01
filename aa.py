import torch

print("go")
print(torch.cuda.is_available())
x = torch.Tensor(10).random_(0, 10)
x.to("cuda")


