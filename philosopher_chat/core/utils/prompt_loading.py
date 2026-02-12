from functools import lru_cache
from pathlib import Path

import yaml


@lru_cache(maxsize=32)
def _load_templates() -> dict[str, str]:
    prompt_path = Path(__file__).parent.parent / "data" / "prompt_template.yaml"
    data = yaml.safe_load(prompt_path.read_text(encoding="utf-8"))
    return data["prompt"]


def load_prompt(input_text: str, philosopher: str) -> dict[str, str]:
    template_config = _load_templates()
    format_args = {"input_text": input_text, "philosopher": philosopher}
    template_config = template_config.format(**format_args)
    return template_config
