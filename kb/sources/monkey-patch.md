---
source: https://en.wikipedia.org/wiki/Monkey_patch
description: "Wikipedia's definition and etymology of monkey patching, with warnings about incompatibility, overwritten patches, debugging confusion, and malicious patch conflicts"
captured: 2026-08-19
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Monkey patch

Author: Wikipedia contributors
Source: https://en.wikipedia.org/wiki/Monkey_patch
Date: Last revised 2026-05-20

**Monkey patch** is the act of dynamically modifying the runtime code (not the [source code](https://en.wikipedia.org/wiki/Source_code)) of a [dynamic programming language](https://en.wikipedia.org/wiki/Dynamic_programming_language), and it is the information (data/code) used to modify the runtime code. Monkey patching adds or replaces programming aspects like [methods](https://en.wikipedia.org/wiki/Method_(computer_science)), [classes](https://en.wikipedia.org/wiki/Class_(programming)), [attributes](https://en.wikipedia.org/wiki/Attribute_(computing)), and [functions](https://en.wikipedia.org/wiki/Subroutine) in [memory](https://en.wikipedia.org/wiki/Computer_memory). Modifying the runtime code allows for modifying the behavior of third-party software without maintaining a modified version of the source code.

The term *monkey patch* seems to have come from an earlier term, *guerrilla patch*, which referred to changing code sneakily — and possibly incompatibly with other such patches — at runtime. The word *[guerrilla](https://en.wikipedia.org/wiki/Guerrilla_warfare)*, nearly homophonous with *[gorilla](https://en.wikipedia.org/wiki/Gorilla)*, became *monkey*, possibly to make the patch sound less intimidating.[^1]

Despite the name's suggestion, a monkey patch is sometimes the official method of extending a program. For example, web browsers such as [Firefox](https://en.wikipedia.org/wiki/Firefox) and [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer) used to encourage this, although today browsers (including Firefox) support extension differently.[^2]

Monkey patch varies depending upon context. In [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)),[^3] [Python](https://en.wikipedia.org/wiki/Python_(programming_language)),[^4] and other languages, monkey patch refers only to dynamic modification of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as desired. Other forms of modifying classes at runtime have different names. For example, in [Zope](https://en.wikipedia.org/wiki/Zope) and [Plone](https://en.wikipedia.org/wiki/Plone_(software)), security patches are often delivered using dynamic class modification, but they are called *hot fixes*.

## Pitfalls

Some pitfalls of monkey patching:

### Incompatibility

A new release of the patched software may break the patch. For this reason, a monkey patch may be conditional and thus only applied if appropriate.[^5]

### Overwriting

If the same [method](https://en.wikipedia.org/wiki/Method_(computer_science)) is patched multiple times, then only the last one is used; the other patches have no effect, unless monkey patches are written with a pattern like *alias_method_chain*.[^6]

### Confusion

A monkey patch creates a discrepancy between the source code and actual behavior that can confuse developers. For example, the [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel) detects proprietary and other third-party modules such as the [Nvidia](https://en.wikipedia.org/wiki/Nvidia) driver, which tamper with kernel structures, so that developers will not waste their time trying to debug a problem that they cannot fix.[^7]

### Chaos

A monkey patch can contain malicious code that attacks the program, or other patches. For example, in 2009, Giorgio Maone, developer of [NoScript](https://en.wikipedia.org/wiki/NoScript), attacked the [Adblock Plus](https://en.wikipedia.org/wiki/Adblock_Plus) extension for Firefox, adding exceptions so that advertisements on his websites would work. The offending code also made sure that if the user attempted to remove the exceptions, they would be added again. An escalating war ensued with new adblock rules pushed to users, followed by Maone sabotaging them, which eventually led to Mozilla stepping in to change policies regarding add-ons.[^8]

## Examples

The following monkey patches the value of [pi](https://en.wikipedia.org/wiki/Pi) in the standard Python math library to make it compliant with the [Indiana pi bill](https://en.wikipedia.org/wiki/Indiana_Pi_Bill).

```pycon
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3.2   # monkey-patch the value of Pi in the math module
>>> math.pi
3.2
```

The next time Python is started, the value of pi will be what it was before the patch: `3.141592653589793`.

## See also

- [Advice](https://en.wikipedia.org/wiki/Advice_(programming))
- [Aspect-oriented programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming)
- [Dynamic loading](https://en.wikipedia.org/wiki/Dynamic_loading)
- [Extension method](https://en.wikipedia.org/wiki/Extension_method)
- [Objective-C category](https://en.wikipedia.org/wiki/Objective-C#Categories)
- [Polyfill](https://en.wikipedia.org/wiki/Polyfill_(programming))
- [Self-modifying code](https://en.wikipedia.org/wiki/Self-modifying_code)

## References

[^1]: ["Glossary — Definition of 'Monkey patch'"](https://docs.plone.org/appendices/glossary.html#term-Monkey-patch), Plone Content Management System. Archived [2021-01-22](https://web.archive.org/web/20210122092034/https://docs.plone.org/appendices/glossary.html#term-Monkey-patch). Accessed 2021-07-02.
[^2]: Arjun Guha, Matthew Fredrikson, Benjamin Livshits, and Nikhil Swamy, "Verified Security for Browser Extensions," *2011 IEEE Symposium on Security and Privacy*, pp. 115–130. [doi:10.1109/SP.2011.36](https://doi.org/10.1109/SP.2011.36).
[^3]: Charles Oliver Nutter, ["Refining Ruby"](http://blog.headius.com/2012/11/refining-ruby.html).
[^4]: Bimal Biswal, ["Monkey Patching in Python"](https://web.archive.org/web/20120822051047/http://www.mindfiresolutions.com/Monkey-Patching-in-Python-1238.php), Mindfire Solutions. Accessed 2013-12-09.
[^5]: Nicholas C. Zakas, ["Maintainable JavaScript: Don't modify objects you don't own"](https://humanwhocodes.com/blog/2010/03/02/maintainable-javascript-dont-modify-objects-you-down-own/), 2010-03-02.
[^6]: ["New in Rails: Module#alias_method_chain"](https://rubyonrails.org/2006/4/26/new-in-rails-module-alias_method_chain), Ruby on Rails.
[^7]: ["Tainted kernels"](https://www.kernel.org/doc/html/v4.15/admin-guide/tainted-kernels.html), Linux Kernel documentation. Accessed 2020-07-12.
[^8]: Ryan Paul, ["Mozilla ponders policy change after Firefox extension battle"](https://arstechnica.com/information-technology/2009/05/mozilla-ponders-policy-change-after-firefox-extension-battle/), Ars Technica, 2009-05-04.
