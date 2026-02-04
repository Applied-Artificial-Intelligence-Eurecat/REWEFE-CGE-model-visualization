from typing import List

import httpx

from src.section import Section, Table


def ask_cge(messages, sections: List[Section], scenario: str, scenario_description: str):
    messages = list(map(lambda m: {key: value for key, value in m.items() if key in [
        "role", "content"]}, messages))
    payload = {
        "messages": messages,
        "scenario": scenario,
        "scenario_description": scenario_description,
        "sections": {section.anchor:
            {
                "title": section.title,
                "anchor": section.anchor,
                "description": section.description,
                "data": {
                    id_: {
                        "id": id_,
                        "data_type": "table" if isinstance(data, Table) else "figure",
                        "caption": data.caption,
                        "notes": data.notes
                    }
                    for id_, data in section.data.items()
                }
            }
            for section in sections
        }
    }
    with httpx.stream("POST", "https://innwater.eurecatprojects.com/assistant/api/cge/cge_tool",
                      json=payload, timeout=70) as response:
        yield from response.iter_text()


def ask_fragments(messages):
    messages = list(map(lambda m: {key: value for key, value in m.items() if key in [
        "role", "content"]}, messages))
    with httpx.stream("POST", "https://innwater.eurecatprojects.com/assistant/api/query/water_tool",
                      json={"messages": messages}, timeout=20) as response:
        yield from response.iter_text()


def ask_to_ai_assistant(ui_messages, scenario_title, scenario_description, sections: List[Section]):
    markdown_sections = '\n'.join(list(map(lambda s: s.to_markdown(), sections)))
    # question = ui_messages[-1]['content']
    # PROMPT = """
    #
    ## {title}
    # {description}
    #
    # Question: {question}
    # """.format(title=scenario_title, description=scenario_description, markdown_sections=markdown_sections,
    #           question=question)
    # messages = list(ui_messages)
    # messages.pop(-1)
    # messages.append({"role": "user", "content": question})
    yield from ask_cge(ui_messages, sections, scenario_title, scenario_description)
