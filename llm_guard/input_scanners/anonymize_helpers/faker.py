from __future__ import annotations

import string
from typing import Any, Callable, cast

from faker import Faker
import random

# 创建中文假数据生成器
fake = Faker(['zh_CN'])
fake.seed_instance(100)


def generate_chinese_id() -> str:
    """生成中国身份证号"""
    # 随机生成地区码(6位)
    area_code = str(random.randint(110000, 659900))
    # 随机生成年月日(8位)
    birth_day = fake.date_of_birth().strftime("%Y%m%d")
    # 随机生成序号(3位)
    sequence = str(random.randint(100, 999))
    # 计算校验码
    temp = int(area_code + birth_day + sequence)
    check_code = '10X98765432'[temp % 11]
    return f"{area_code}{birth_day}{sequence}{check_code}"


def generate_social_credit_code() -> str:
    """生成统一社会信用代码"""
    organization_code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))
    category_code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
    area_code = ''.join(random.choices('0123456789', k=6))
    check_code = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
    return f"{organization_code}{category_code}{area_code}{check_code}"


_entity_faker_map: dict[str, Callable[[], Any]] = {
    # 保留原有的全局实体
    "CREDIT_CARD": fake.credit_card_number,
    "EMAIL_ADDRESS": fake.email,
    "IP_ADDRESS": fake.ipv4_public,
    "PERSON": fake.name,
    "URL": fake.url,
    "UUID": fake.uuid4,
    "LOCATION": fake.city,
    "DATE_TIME": fake.date,

    # 添加中国特定的实体
    "PHONE_NUMBER_CN": lambda: f"1{random.choice(['3', '4', '5', '6', '7', '8', '9'])}{fake.numerify('########')}",
    "ID_CARD_CN": generate_chinese_id,
    "BANK_CARD_CN": lambda: f"{random.choice(['4', '5', '6'])}{fake.numerify('#' * 15)}",
    "SOCIAL_CREDIT_CODE_CN": generate_social_credit_code,
    "POSTAL_CODE_CN": lambda: fake.postcode(),
    "PASSPORT_CN": lambda: f"{random.choice(['E', 'G', 'D', 'S'])}{fake.numerify('########')}",
    "MILITARY_ID_CN": lambda: f"军字第{fake.numerify('########')}号",
    "QQ_NUMBER": lambda: str(random.randint(10000, 9999999999)),
    "WECHAT_ID": lambda: f"wx_{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}",
    "LICENSE_PLATE_CN": lambda: f"{random.choice('京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领')}{random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')}{''.join(random.choices('0123456789ABCDEFGHJKLMNPQRSTUVWXYZ', k=5))}",

    # 中国其他常见证件号码
    "PASSPORT_HK_CN": lambda: f"H{fake.numerify('########')}",
    "PASSPORT_MO_CN": lambda: f"M{fake.numerify('########')}",
    "PASSPORT_TW_CN": lambda: f"T{fake.numerify('########')}",
    "HK_ID_CN": lambda: f"{random.choice(string.ascii_uppercase)}{fake.numerify('######')}({random.choice(string.digits)})",
    "MO_ID_CN": lambda: f"{fake.numerify('#######')}({random.choice(string.digits)})",

    # 公司相关
    "TAX_ID_CN": lambda: f"{fake.numerify('####################')}",
    "ORGANIZATION_CODE_CN": lambda: f"{fake.numerify('########')}-{random.choice(string.digits)}",

    # 其他中国特色号码
    "ALIPAY_ID": lambda: f"2088{fake.numerify('##########')}",
    "WEBSITE_ICP": lambda: f"京ICP备{fake.numerify('#####')}号",
}


def get_fake_value(entity_type: str) -> str | None:
    if entity_type not in _entity_faker_map:
        return None

    return _entity_faker_map[entity_type]()
