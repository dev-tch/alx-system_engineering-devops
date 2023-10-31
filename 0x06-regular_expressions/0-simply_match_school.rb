#!/usr/bin/env ruby
#  create a Ruby script that accepts one argument and pass it to a regular expression matching method
pattern=/School/

result_match = ""

if ARGV.length >= 1
  input  = ARGV[0]
  # scan return array --> join will return string from array 
  result_match  = input.scan(pattern).join
end
puts result_match
