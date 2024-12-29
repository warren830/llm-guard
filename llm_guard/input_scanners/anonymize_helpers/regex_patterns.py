from __future__ import annotations

from typing import TypedDict

from llm_guard.util import get_logger

LOGGER = get_logger()


class DefaultRegexPatterns(TypedDict):
    name: str
    expressions: list[str]
    examples: list[str]
    context: list[str]
    score: float
    languages: list[str]


class RegexPatternsReuse(TypedDict):
    name: str
    languages: list[str]
    reuse: dict[str, str]


class RegexPattern(TypedDict):
    name: str
    expressions: list[str]
    context: list[str]
    score: float
    languages: list[str]
    reuse: dict[str, str] | None


DEFAULT_REGEX_PATTERNS: list[DefaultRegexPatterns | RegexPatternsReuse] = [
    {
        "expressions": [
            r"(?:(4\d{3}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4})|(3[47]\d{2}[-\s]?\d{6}[-\s]?\d{5})|(3(?:0[0-5]|[68]\d)\d{11}))"
        ],
        "name": "CREDIT_CARD_RE",
        "examples": ["4111111111111111", "378282246310005", "30569309025904"],
        "context": [],
        "score": 0.75,
        "languages": ["en", "zh"],
    },
    {
        "expressions": [r"[a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12}"],
        "name": "UUID",
        "examples": ["550e8400-e29b-41d4-a716-446655440000"],
        "context": [],
        "score": 0.75,
        "languages": ["en", "zh"],
    },
    {
        "expressions": [r"\b[A-Za-z0-9._%+-]+(\[AT\]|@)[A-Za-z0-9.-]+(\[DOT\]|\.)[A-Za-z]{2,}\b"],
        "name": "EMAIL_ADDRESS_RE",
        "examples": [
            "john.doe@protectai.com",
            "john.doe[AT]protectai[DOT]com",
            "john.doe[AT]protectai.com",
            "john.doe@protectai[DOT]com",
        ],
        "context": [],
        "score": 0.75,
        "languages": ["en", "zh"],
    },
    {
        "expressions": [r"\b\d{3}-\d{2}-\d{4}\b"],
        "name": "US_SSN_RE",
        "examples": ["111-22-3333", "987-65-4321"],
        "context": [],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [
            r"(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])"
        ],
        "name": "BTC_ADDRESS",
        "examples": [
            "1LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2",
            "19P6EYhu6kZzRy9Au4wRRZVE8RemrxPbZP",
            "1bones8KbQge9euDn523z5wVhwkTP3uc1",
            "1Bow5EMqtDGV5n5xZVgdpRPJiiDK6XSjiC",
        ],
        "context": [],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [
            r"(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|(?:construction)|(?:contractors)|(?:enterprises)|(?:photography)|(?:immobilien)|(?:management)|(?:technology)|(?:directory)|(?:education)|(?:equipment)|(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|(?:computer)|(?:democrat)|(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|(?:careers)|(?:company)|(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|(?:berlin)|(?:camera)|(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|(?:monash)|(?:museum)|(?:photos)|(?:repair)|(?:social)|(?:tattoo)|(?:travel)|(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|(?:email)|(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|(?:arpa)|(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|(?:guru)|(?:info)|(?:jobs)|(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|(?:uno)|(?:xxx)|(?:ac)|(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|(?:su)|(?:sv)|(?:sx)|(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'\".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)"
        ],
        "name": "URL_RE",
        "examples": ["http://www.protectai.com", "https://protectai.com", "www.protectai.com"],
        "context": [],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "name": "CREDIT_CARD",
        "reuse": {"language": "en", "name": "CREDIT_CARD"},
        "languages": ["zh"],
    },
    {
        "expressions": [r"[A-Za-z0-9._%+-]+(\[AT\]|@)[A-Za-z0-9.-]+(\[DOT\]|\.)[A-Za-z]{2,}"],
        "name": "EMAIL_ADDRESS_RE",
        "examples": [
            "john.doe@protectai.com",
            "john.doe[AT]protectai[DOT]com",
            "john.doe[AT]protectai.com",
            "john.doe@protectai[DOT]com",
        ],
        "context": [],
        "score": 0.75,
        "languages": ["zh"],
    },
    {
        "expressions": [r"(13[0-9]|14[5-9]|15[0-3,5-9]|16[6]|17[0-8]|18[0-9]|19[8,9])\d{8}"],
        "name": "PHONE_NUMBER_ZH",
        "examples": ["13011112222", "14922223333"],
        "context": ["phone", "number", "telephone", "cell", "cellphone", "mobile", "call"],
        "score": 0.75,
        "languages": ["zh"],
    },
    {
        "expressions": [
            r"(?i)((?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?(?:[2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?(?:[0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(?:\d+)?))"
        ],
        "name": "PHONE_NUMBER_WITH_EXT",
        "examples": [
            "(523)222-8888 ext 527",
            "(523)222-8888x623",
            "(523)222-8888 x623",
            "(523)222-8888 x 623",
            "(523)222-8888EXT623",
            "523-222-8888EXT623",
            "(523) 222-8888 x 623",
        ],
        "context": [],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [
            r"(?i)(?:(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}"
        ],
        "name": "DATE_RE",
        "examples": [
            "12-31-2024",
            "12/31/2024",
            "3 of April 2021",
            "3rd of April 2021",
            "November 30th 2021",
            "November 30 2021",
            "4th July, 2022",
        ],
        "context": ["date", "time", "month", "year"],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [r"(?i)\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?"],
        "name": "TIME_RE",
        "examples": ["12:00 PM", "12:00PM", "12:00 pm", "12:00pm", "12:00", "12pm"],
        "context": ["time"],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [r"(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\b"],
        "name": "HEX_COLOR",
        "examples": ["#ff0000", "#f00"],
        "context": ["color", "code"],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [r"[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?"],
        "name": "PRICE_RE",
        "examples": ["$1.23", "$1", "$1,000", "$10,000.00"],
        "context": ["price", "money", "cost", "value", "amount"],
        "score": 0.75,
        "languages": ["en"],
    },
    {
        "expressions": [r"(?i)P\.? ?O\.? Box \d+"],
        "name": "PO_BOX_RE",
        "examples": ["PO Box 123456", "hey p.o. box 234234 hey"],
        "context": ["address", "mail", "post", "box"],
        "score": 0.75,
        "languages": ["en"],
    },
    # 中国手机号
    {
        "expressions": [
            r"(?:(?:\+|00)86)?1(?:3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}"
        ],
        "name": "PHONE_NUMBER_CN",
        "examples": ["13812345678", "+8613812345678", "008613812345678"],
        "context": ["电话", "手机", "联系方式", "phone", "mobile"],
        "score": 0.75,
        "languages": ["zh", "en"],
    },

    # 中国身份证号
    {
        "expressions": [
            r"[1-9]\d{5}(?:18|19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]"
        ],
        "name": "ID_CARD_CN",
        "examples": ["110101199001011234", "11010119900101123X"],
        "context": ["身份证", "身份证号", "身份证号码", "公民身份号码"],
        "score": 0.95,  # 提高身份证的匹配优先级
        "languages": ["zh"],
    },

    # 中国银行卡号
    {
        "expressions": [
            r"([1-9])(\d{15}|\d{18})"
        ],
        "name": "BANK_CARD_CN",
        "examples": ["6222021234567890123"],
        "context": ["银行卡", "储蓄卡", "信用卡", "bank card"],
        "score": 0.75,
        "languages": ["zh", "en"],
    },

    # 统一社会信用代码
    {
        "expressions": [
            r"[1-9A-GY]{1}[1239]{1}[1-5]{1}[0-9]{5}[0-9A-Z]{10}"
        ],
        "name": "SOCIAL_CREDIT_CODE_CN",
        "examples": ["91110108MA01234567"],
        "context": ["统一社会信用代码", "营业执照", "企业代码"],
        "score": 0.75,
        "languages": ["zh"],
    },

    # 中国邮政编码
    {
        "expressions": [
            r"[1-9]\d{5}(?!\d)"
        ],
        "name": "POSTAL_CODE_CN",
        "examples": ["100000"],
        "context": ["邮编", "邮政编码", "postal code"],
        "score": 0.75,
        "languages": ["zh", "en"],
    },

    # 护照号码
    {
        "expressions": [
            r"[EGPS]\d{8}|[DES][A-Z]\d{7}"
        ],
        "name": "PASSPORT_CN",
        "examples": ["E12345678", "DE1234567"],
        "context": ["护照", "passport"],
        "score": 0.75,
        "languages": ["zh", "en"],
    },

    # 军官证号码
    {
        "expressions": [
            r"[\u4e00-\u9fa5]{1,2}字第\d{4,8}号"
        ],
        "name": "MILITARY_ID_CN",
        "examples": ["军字第2001234号", "军官字第2001234号"],
        "context": ["军官证", "军人证件"],
        "score": 0.75,
        "languages": ["zh"],
    },

    # QQ号
    {
        "expressions": [
            r"[1-9][0-9]{4,}"
        ],
        "name": "QQ_NUMBER",
        "examples": ["12345678", "1234567890"],
        "context": ["QQ", "腾讯", "qq号"],
        "score": 0.75,
        "languages": ["zh"],
    },

    # 微信号
    {
        "expressions": [
            r"[a-zA-Z][-_a-zA-Z0-9]{5,19}"
        ],
        "name": "WECHAT_ID",
        "examples": ["wxid_1234567890", "wx_12345"],
        "context": ["微信", "WeChat", "微信号"],
        "score": 0.75,
        "languages": ["zh"],
    },

    # 车牌号
    {
        "expressions": [
            r"[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z][A-HJ-NP-Z0-9]{4,5}[A-HJ-NP-Z0-9挂学警港澳]"
        ],
        "name": "LICENSE_PLATE_CN",
        "examples": ["京A12345", "粤B12345D"],
        "context": ["车牌", "车牌号", "车辆号码"],
        "score": 0.75,
        "languages": ["zh"],
    },
]


def get_regex_patterns(
    regex_patterns: list[DefaultRegexPatterns | RegexPatternsReuse] | None = None,
) -> list[RegexPattern]:
    if not regex_patterns:
        regex_patterns = DEFAULT_REGEX_PATTERNS

    result: list[RegexPattern] = []
    for group in regex_patterns:
        result.append(
            {
                "name": group["name"].upper(),
                "expressions": group.get("expressions", []),
                "context": group.get("context", []),
                "score": group.get("score", 0.75),
                "languages": group.get("languages", ["en"]),
                "reuse": group.get("reuse", None),
            }
        )
        LOGGER.debug("Loaded regex pattern", group_name=group["name"])

    return result
