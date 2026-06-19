from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://mainsite-aiyouxi.com.cn"
SAMPLE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """关键词笔记的数据类"""
    keyword: str
    url: str
    title: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    note: str = ""

    def summary(self, max_keyword_len: int = 10) -> str:
        """返回摘要文本"""
        kw = self.keyword[:max_keyword_len]
        return f"[{kw}] {self.url} — {self.note[:30] if self.note else '无备注'}"

    def formatted_block(self, line_width: int = 60) -> str:
        """返回格式化的笔记块"""
        sep = "─" * line_width
        lines = [sep]
        lines.append(f" 关键词：{self.keyword}")
        lines.append(f" 网址：  {self.url}")
        if self.title:
            lines.append(f" 标题：  {self.title}")
        if self.tags:
            lines.append(f" 标签：  {', '.join(self.tags)}")
        lines.append(f" 创建：  {self.created_at.strftime('%Y-%m-%d %H:%M')}")
        if self.note:
            lines.append(f" 备注：  {self.note}")
        lines.append(sep)
        return "\n".join(lines)


def create_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记"""
    return [
        KeywordNote(
            keyword="爱游戏",
            url=SAMPLE_URL,
            title="爱游戏官方网站",
            tags=["游戏", "平台"],
            note="主要游戏资讯与社区入口。"
        ),
        KeywordNote(
            keyword="爱游戏攻略",
            url=f"{SAMPLE_URL}/guides",
            title="攻略中心",
            tags=["攻略", "教程"],
            note="包含各热门游戏的详细攻略。"
        ),
        KeywordNote(
            keyword="爱游戏活动",
            url=f"{SAMPLE_URL}/events",
            tags=["活动", "福利"],
            note="限时活动和礼包码汇总。"
        ),
    ]


def print_all_notes(notes: List[KeywordNote]) -> None:
    """打印所有笔记到控制台"""
    for i, note in enumerate(notes, 1):
        print(f"\n笔记 #{i}")
        print(note.formatted_block())


def format_notes_as_text(notes: List[KeywordNote]) -> str:
    """将所有笔记拼接为一个纯文本字符串"""
    parts = []
    for i, note in enumerate(notes, 1):
        parts.append(f"=== 笔记 #{i} ===")
        parts.append(note.formatted_block())
    return "\n".join(parts)


def find_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """按标签查找笔记，返回匹配列表"""
    return [n for n in notes if tag.lower() in [t.lower() for t in n.tags]]


def main():
    """演示函数"""
    demo_notes = create_sample_notes()

    print("所有关键词笔记：")
    print_all_notes(demo_notes)

    print("\n查找标签为 '活动' 的笔记：")
    found = find_notes_by_tag(demo_notes, "活动")
    for note in found:
        print(f" - {note.keyword} ({note.url})")

    print("\n纯文本导出示例（前200字符）：")
    txt = format_notes_as_text(demo_notes)
    print(txt[:200])


if __name__ == "__main__":
    main()