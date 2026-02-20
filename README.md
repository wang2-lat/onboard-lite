# onboard-lite

Lightweight user onboarding tool for startups - create product tours without expensive SaaS.

## Problem

Expensive tools like Pendo cost hundreds of dollars per month. Small teams with few users only need basic functionality to show new users how to use their product. This tool provides exactly that - no more, no less.

## Installation


## Usage

### 1. Create a tour configuration


This creates a sample YAML file with tour steps. Edit it to match your product:


### 2. Preview the tour


### 3. Generate embeddable code


Copy the generated code and paste it into your webpage before the `</body>` tag.

## Configuration Format

- `target`: CSS selector for the element to highlight
- `title`: Step title
- `content`: Step description
- `position`: Tooltip position (bottom, top, left, right)

## Features

- Zero dependencies in generated code
- Works with any website
- Lightweight and fast
- Easy to customize

## License

MIT
# 1. 安装依赖
pip install -r requirements.txt

# 2. 创建配置
python main.py create --output tour.yaml

# 3. 预览效果
python main.py preview tour.yaml

# 4. 生成代码
python main.py generate tour.yaml --output tour.html