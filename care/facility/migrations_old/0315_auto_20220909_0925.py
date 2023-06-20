# Generated by Django 2.2.11 on 2022-09-09 03:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations

import care.utils.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0314_patientconsultation_icd11_diagnoses"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyround",
            name="pain_scale_enhanced",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=list,
                validators=[
                    care.utils.models.validators.JSONFieldSchemaValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "items": [
                                {
                                    "additionalProperties": False,
                                    "properties": {
                                        "description": {"type": "string"},
                                        "region": {"type": "string"},
                                        "scale": {
                                            "maximum": 5,
                                            "minimum": 1,
                                            "type": "number",
                                        },
                                    },
                                    "required": ["region", "scale"],
                                    "type": "object",
                                }
                            ],
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="dailyround",
            name="pressure_sore",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=list,
                validators=[
                    care.utils.models.validators.JSONFieldSchemaValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "items": [
                                {
                                    "additionalProperties": False,
                                    "properties": {
                                        "description": {"type": "string"},
                                        "region": {"type": "string"},
                                        "scale": {
                                            "maximum": 5,
                                            "minimum": 1,
                                            "type": "number",
                                        },
                                    },
                                    "required": ["region", "scale"],
                                    "type": "object",
                                }
                            ],
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
    ]