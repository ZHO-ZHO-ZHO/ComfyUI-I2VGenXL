
![I2V_](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/3d2acebe-b4b4-417a-8257-427b3fd33680)


# ComfyUI I2VGenXL

Unofficial implementation of [I2VGenXL](https://i2vgen-xl.github.io/) for ComfyUI


https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/f76b9a29-4aad-4696-9cde-6690eb48a16e


## 项目介绍 | Info

- 对[I2VGenXL](https://i2vgen-xl.github.io/)的非官方实现，实测下来是目前 **动效自然程度** 和 **光影** 最好的 **高清** 视频模型（幅度没有SVD1.1大，但是综合效果比 SVD1.1 强）

- I2VGenXL 特点：
  - 与 SVD 不同，I2VGenXL 可以通过输入正负提示词来完成更好的生成
  - 分辨率：1280*704
  - 生成帧数：16帧
  - 速度：A100约97s（比 SVD1.1 慢 20%）

- 版本：V1.0 


# 视频演示

文/图生视频标准工作流设计

https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/53096355-2235-40f4-9668-b7965172f0b2


## 节点说明 | Features

- 模型加载 | 📽️I2VGenXL Model Loader
    - 自动下载并加载官方 ali-vilab/i2vgen-xl 模型

- I2VGenXL 生成 | 📽️I2VGenXL Generation
    - pipe：接入模型
    - image：接入图像
    - positivet、negative：正负提示词
    - step：步数，官方默认50步
    - guidance_scale：提示词相关度，一般7.5-9
    - width、height：宽度、高度
    - num_frames：生成帧数
    - seed：种子


![Dingtalk_20240206191942](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/d88dec90-79a3-4ea0-8fed-168e8f3a7df4)

 
## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装（On the Way）

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL.git`
    3. `cd custom_nodes/ComfyUI-I2VGenXL`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI


## 使用注意 | Note

- 模型有一定概率会出现最后一帧空白的情况，暂不清楚是什么原因，所以目前节点直接删除了最后一帧，所以默认生成结果是15帧


## 工作流 | Workflows

V1.0

- **标准工作流设计**：

   - 参考了 [stablevideo.com](https://stablevideo.com) 的 UI 交互逻辑，与我设计的 SVD1.1 标准工作流相同
  
   - 支持文生视频和图生视频两种方式：其中文生视频支持自动暂停选择图像，满意之后再运行视频生成
  
   - 加入了自动补帧插件
  
   - 使用插件：[cg-image-picker](https://github.com/chrisgoringe/cg-image-picker)，[ComfyUI-SVD-ZHO](https://github.com/ZHO-ZHO-ZHO/ComfyUI-SVD-ZHO)，[ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation)，[rgthree-comfy](https://github.com/rgthree/rgthree-comfy)，[ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
  
   - 工作流文件：[V1.0 Standard 标准版](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/blob/main/I2VGENXL%20WORKFLOWS/I2VGENXL_Standard%E3%80%90Zho%E3%80%91.json)
  
  ![Dingtalk_20240206191614](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/05c9a690-110b-4f42-b4a3-aa8f7a0f3e3f)

- 基础工作流：[V1.0 Simple 基础版](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/blob/main/I2VGENXL%20WORKFLOWS/I2VGENXL_Simple%E3%80%90Zho%E3%80%91.json)

  ![Dingtalk_20240206193817](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/d33f3238-d6ad-4e00-b1de-a36f156e7485)



## 更新日志

- 20240206

  V1.0 优化代码，并设计标准工作流

- 20240205

  创建项目


## 速度实测 | Speed

- V1.0 

    - A100 50步 97s

    ![image](https://github.com/ZHO-ZHO-ZHO/ComfyUI-I2VGenXL/assets/140084057/f2575b23-eea9-46d7-a89f-ec5f6e21e534)




## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-I2VGenXL&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-I2VGenXL&Date)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[I2VGenXL](https://i2vgen-xl.github.io/)
