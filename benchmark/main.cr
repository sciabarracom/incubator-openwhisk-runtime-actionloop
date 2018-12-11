def main(args)
  if name = args["name"]?
    return {"greeting" => "Hello #{name}!"}
  else
    return {"greeting" => "Hello crystal world!"}
  end
end
