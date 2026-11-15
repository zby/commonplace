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
          not: {required: [attack-outcome]}
        else:
          required: [attack-outcome]
          properties:
            outcome: {const: report}
            findings: {items: {not: {required: [level]}}}
      - if: {properties: {outcome: {enum: [warn, fail]}}}
        then: {properties: {findings: {minItems: 1}}}
      - if: {properties: {outcome: {const: pass}}}
        then: {properties: {findings: {items: {properties: {level: {const: info}}}}}}
  body: {type: string, minLength: 1}
  headings:
    type: array
    contains: {pattern: '^# '}
allOf:
  - if: {properties: {frontmatter: {properties: {contract: {const: report}}}}}
    then:
      properties:
        headings:
          allOf:
            - contains: {const: '## Strongest case against it'}
            - contains: {const: '## How the note engages it'}
            - contains: {const: '## Constructive findings'}
$defs:
  digest: {type: string, pattern: '^[0-9a-f]{64}$'}
  path: {type: string, minLength: 1, pattern: '^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[^\\]+$'}
