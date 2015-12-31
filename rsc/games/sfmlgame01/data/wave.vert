uniform float wave_phase;
uniform vec2 wave_amplitude;

void main()
{
    vec4 vertex = gl_Vertex;
    vertex.x += cos(gl_Vertex.y * 0.025 + wave_phase * 3.8) * wave_amplitude.x;
    vertex.y += sin(gl_Vertex.x * 0.025 + wave_phase * 2.4) * wave_amplitude.y;

	gl_Position = gl_ModelViewProjectionMatrix * vertex;
	gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;
	gl_FrontColor = gl_Color;
}
