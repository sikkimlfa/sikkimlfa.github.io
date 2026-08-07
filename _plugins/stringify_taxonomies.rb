Jekyll::Hooks.register :posts, :pre_render do |post|
  if post.data['categories'].is_a?(Array)
    post.data['categories'] = post.data['categories'].map(&:to_s)
  end

  if post.data['tags'].is_a?(Array)
    post.data['tags'] = post.data['tags'].map(&:to_s)
  end
end
