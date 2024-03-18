from torch.utils.data import Dataset,DataLoader
import torchvision.transforms as transforms


class CustomDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data[idx]
        label = self.labels[idx]
        if self.transform:
            image = self.transform(image)
        return image, label


# 假设您已经有一个包含图像和标签的列表
images = [...]
labels = [...]

# 定义数据增强（可选）
transform = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)

# 创建数据集实例
dataset = CustomDataset(images, labels, transform=transform)

# 创建数据加载器
dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)
