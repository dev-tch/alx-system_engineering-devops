#!/usr/bin/env ruby
# The regular expression must be only matching: capital letters
pattern=/[A-Z]+/
result_match = ""

if ARGV.length >= 1
  input  = ARGV[0]
  result_match = input.scan(pattern).join
end
puts result_match
