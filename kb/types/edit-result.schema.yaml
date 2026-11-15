$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required: [frontmatter, body, headings]
properties:
  frontmatter:
    type: object
    additionalProperties: false
    required: [type, description, format, outcome, operation, operation-sha256, note, input-sha256,
               candidate, candidate-sha256, observation, contract-sha256, profile, model, run, launch,
               completed-at, raw-output, raw-output-sha256]
    properties:
      type: {const: types/edit-result.md}
      description: {type: string, minLength: 1}
      format: {const: 1}
      outcome: {enum: [changed, unchanged, proposed, problem]}
      changes:
        type: array
        items: {type: string, minLength: 1}
      proposals:
        type: array
        items:
          type: object
          additionalProperties: false
          required: [quote, change, reason]
          properties:
            quote: {type: string, minLength: 1}
            change: {type: string, minLength: 1}
            reason: {type: string, minLength: 1}
      removed-links:
        type: array
        items: {type: string, minLength: 1}
      operation: {type: string, minLength: 1}
      operation-sha256: {$ref: '#/$defs/digest'}
      note: {$ref: '#/$defs/path'}
      input-sha256: {$ref: '#/$defs/digest'}
      candidate: {anyOf: [{$ref: '#/$defs/path'}, {type: 'null'}]}
      candidate-sha256: {anyOf: [{$ref: '#/$defs/digest'}, {type: 'null'}]}
      observation: {$ref: '#/$defs/path'}
      contract-sha256: {$ref: '#/$defs/digest'}
      profile: {type: object}
      model: {type: [string, 'null']}
      run: {$ref: '#/$defs/path'}
      launch: {type: string, minLength: 1}
      completed-at: {type: string, format: date-time}
      raw-output: {anyOf: [{$ref: '#/$defs/path'}, {type: 'null'}]}
      raw-output-sha256: {anyOf: [{$ref: '#/$defs/digest'}, {type: 'null'}]}
    allOf:
      - if: {properties: {outcome: {const: changed}}}
        then:
          required: [changes]
          properties:
            changes: {minItems: 1}
            candidate: {type: string}
            candidate-sha256: {type: string}
          not: {required: [proposals]}
      - if: {properties: {outcome: {const: unchanged}}}
        then:
          properties:
            changes: {maxItems: 0}
            candidate: {type: string}
            candidate-sha256: {type: string}
          not: {anyOf: [{required: [proposals]}, {required: [removed-links]}]}
      - if: {properties: {outcome: {const: proposed}}}
        then:
          required: [proposals]
          properties:
            proposals: {minItems: 1}
            candidate: {type: 'null'}
            candidate-sha256: {type: 'null'}
          not: {anyOf: [{required: [changes]}, {required: [removed-links]}]}
      - if: {properties: {outcome: {const: problem}}}
        then:
          properties:
            candidate: {type: 'null'}
            candidate-sha256: {type: 'null'}
            raw-output: {type: 'null'}
            raw-output-sha256: {type: 'null'}
          not: {anyOf: [{required: [changes]}, {required: [proposals]}, {required: [removed-links]}]}
        else:
          properties:
            raw-output: {type: string}
            raw-output-sha256: {type: string}
  body: {type: string, minLength: 1}
  headings:
    type: array
    contains: {pattern: '^# '}
$defs:
  digest: {type: string, pattern: '^[0-9a-f]{64}$'}
  path: {type: string, minLength: 1, pattern: '^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[^\\]+$'}
