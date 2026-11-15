$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required: [frontmatter, body, headings]
properties:
  frontmatter:
    type: object
    additionalProperties: false
    required: [type, description, format, contract, findings, outcome, note, criterion,
               note-sha256, criterion-sha256, target-sha256, target-capture,
               observation, contract-sha256, profile, model, run, launch, completed-at,
               raw-output, raw-output-sha256]
    properties:
      type: {const: types/review-result.md}
      description: {type: string, minLength: 1}
      format: {const: 2}
      contract: {enum: [verdict, report]}
      note: {$ref: '#/$defs/path'}
      criterion: {type: string, minLength: 1}
      note-sha256: {$ref: '#/$defs/digest'}
      criterion-sha256: {$ref: '#/$defs/digest'}
      target-sha256: {$ref: '#/$defs/digest'}
      target-capture: {$ref: '#/$defs/path'}
      observation: {$ref: '#/$defs/path'}
      contract-sha256: {$ref: '#/$defs/digest'}
      profile: {type: object}
      model: {type: [string, 'null']}
      run: {$ref: '#/$defs/path'}
      launch: {type: string, minLength: 1}
      completed-at: {type: string, format: date-time}
      raw-output: {$ref: '#/$defs/path'}
      raw-output-sha256: {$ref: '#/$defs/digest'}
      outcome: {enum: [pass, warn, fail, report]}
      attack-outcome:
        enum: [lands, partially lands, no surviving attack, 'no surviving attack (low confidence — needs domain check)']
      findings:
        type: array
        items:
          type: object
          additionalProperties: false
          required: [scope, quotes, reason]
          properties:
            scope: {enum: [passage, document]}
            quotes: {type: array, items: {type: string, minLength: 1}}
            reason: {type: string, minLength: 1}
            level: {enum: [info, warn, fail]}
          allOf:
            - if: {properties: {scope: {const: passage}}}
              then: {properties: {quotes: {minItems: 1}}}
              else: {properties: {quotes: {maxItems: 0}}}
    allOf:
      - if: {properties: {contract: {const: verdict}}}
        then:
          properties:
            outcome: {enum: [pass, warn, fail]}
            findings: {items: {required: [level]}}
            criterion: {not: {$ref: '#/$defs/report-criterion'}}
        else:
          properties:
            outcome: {const: report}
            findings: {items: {not: {required: [level]}}}
            criterion: {$ref: '#/$defs/report-criterion'}
      - if: {required: [criterion], properties: {criterion: {$ref: '#/$defs/critique'}}}
        then: {required: [attack-outcome]}
        else: {not: {required: [attack-outcome]}}
      - if: {required: [criterion], properties: {criterion: {$ref: '#/$defs/friction'}}}
        then:
          properties:
            findings: {items: {properties: {reason: {pattern: '^(UNSUPPORTED|THIN|HOLDS)\b'}}}}
      - if: {required: [criterion], properties: {criterion: {$ref: '#/$defs/premises'}}}
        then:
          properties:
            findings:
              items:
                properties:
                  reason:
                    pattern: '^(HOLDS\b|(DOUBTFUL|DEFEATED)\b(?=[\s\S]*\b(LOCAL|GLOBAL)\b)(?=[\s\S]*\b(instance|prevalence|priced-exception)\b))'
      - if: {required: [criterion], properties: {criterion: {$ref: '#/$defs/synthesis'}}}
        then: {properties: {findings: {maxItems: 3}}}
      - if: {properties: {outcome: {enum: [warn, fail]}}}
        then: {properties: {findings: {minItems: 1}}}
      - if: {properties: {outcome: {const: pass}}}
        then: {properties: {findings: {items: {properties: {level: {const: info}}}}}}
  body: {type: string, minLength: 1}
  headings:
    type: array
    contains: {pattern: '^# '}
allOf:
  - if: {properties: {frontmatter: {required: [criterion], properties: {criterion: {$ref: '#/$defs/critique'}}}}}
    then:
      properties:
        headings:
          allOf:
            - contains: {const: '## Strongest case against it'}
            - contains: {const: '## How the note engages it'}
            - contains: {const: '## Constructive findings'}
  - if: {properties: {frontmatter: {required: [criterion], properties: {criterion: {$ref: '#/$defs/friction'}}}}}
    then:
      properties:
        body: {pattern: '(?m)^\*\*Filter:\*\* (SURVIVES|DISSOLVES)\b'}
        headings:
          allOf:
            - contains: {const: '## Filter'}
            - contains: {const: '## Thinnest joints'}
            - contains: {const: '## For the human'}
  - if: {properties: {frontmatter: {required: [criterion], properties: {criterion: {$ref: '#/$defs/premises'}}}}}
    then:
      properties:
        body: {pattern: '(?m)^\*\*Register:\*\* (claim|definition|procedure)\b'}
        headings:
          allOf:
            - contains: {const: '## Premises and counterexamples'}
            - contains: {const: '## For the human'}
  - if: {properties: {frontmatter: {required: [criterion], properties: {criterion: {$ref: '#/$defs/synthesis'}}}}}
    then:
      properties:
        headings: {contains: {const: '## Opportunities'}}
$defs:
  # A report criterion is named by its library instruction: `kb/<path>` in a
  # Commonplace checkout, `commonplace:<path>` in an installed project.
  critique: {type: string, pattern: '^(kb/|commonplace:)instructions/critique-note\.md$'}
  friction: {type: string, pattern: '^(kb/|commonplace:)instructions/composition-friction-gate\.md$'}
  premises: {type: string, pattern: '^(kb/|commonplace:)instructions/premise-decomposition-gate\.md$'}
  synthesis:
    type: string
    pattern: '^(kb/|commonplace:)instructions/compression-bundle/high-impact-simplification-synthesis\.md$'
  report-criterion:
    anyOf: [{$ref: '#/$defs/critique'}, {$ref: '#/$defs/friction'}, {$ref: '#/$defs/premises'},
            {$ref: '#/$defs/synthesis'}]
  digest: {type: string, pattern: '^[0-9a-f]{64}$'}
  path: {type: string, minLength: 1, pattern: '^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[^\\]+$'}
